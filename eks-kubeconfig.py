import os
import boto3
import configparser
import subprocess
from pathlib import Path
from botocore.exceptions import ClientError

# Function to get profiles with sso_account_id
def get_sso_profiles(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    sso_profiles = []
    for section in config.sections():
        if section.startswith('profile ') and 'sso_account_id' in config[section]:
            # Extract everything after 'profile ' and add it to the list
            profile_name = section.split(' ', 1)[1]
            sso_profiles.append(profile_name)
    return sso_profiles


# Function to list EKS clusters for a profile
def list_eks_clusters(profile):
    try:
        session = boto3.Session(profile_name=profile)
        eks = session.client('eks')
        clusters = eks.list_clusters()['clusters']
        print(f"Found {len(clusters)} EKS clusters for profile {profile}")
        return clusters
    except ClientError as e:
        print(f"Access error listing EKS clusters for profile {profile}: {e}")
        return []

def create_cluster_file(cluster_name, profile):
    filename = f"{cluster_name}.yaml"
    print(f"Creating kubeconfig file for cluster {cluster_name} in file {filename}")
    # Command to generate kubeconfig for the cluster and redirect it to the specific file
    command = f"aws eks update-kubeconfig --name {cluster_name} --profile {profile} --kubeconfig {filename}"
    try:
        # Execute the command
        subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Set file permissions to 600
        os.chmod(filename, 0o600)
        # Change the file's owner to the current user
        user = os.getenv("USER")
        os.system(f'chown {user} {filename}')
    except subprocess.CalledProcessError as e:
        print(f"Failed to create kubeconfig for cluster {cluster_name}: {e}")

    print(f"Kubeconfig file {filename} created successfully")

def main():
    aws_config_path = Path.home() / '.aws/config'
    current_user = os.getenv("USER")
    sso_profiles = get_sso_profiles(aws_config_path)

    for profile in sso_profiles:
        clusters = list_eks_clusters(profile)
        for cluster in clusters:
            create_cluster_file(cluster, profile)

if __name__ == "__main__":
    main()
