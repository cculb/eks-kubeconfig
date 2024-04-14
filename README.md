# EKS Kubeconfig Generator

This Python script generates kubeconfig files for all EKS clusters associated with AWS SSO profiles.

## Description

The script performs the following tasks:

1. Reads the AWS configuration file (`~/.aws/config`) to identify profiles with `sso_account_id`.
2. Lists all EKS clusters for each SSO profile.
3. Creates a kubeconfig file for each EKS cluster, named `<cluster-name>.yaml`.
4. Sets the file permissions of the generated kubeconfig files to 600 and changes the owner to the current user.

## Prerequisites

Before running the script, ensure that you have the following:

- Python 3.x installed
- AWS CLI installed and configured with SSO profiles
- Required Python packages: `boto3`, `configparser`

## Usage

1. Clone the repository or download the `eks-kubeconfig.py` script.

2. Open a terminal and navigate to the directory containing the script.

3. Run the script using the following command:

4. The script will generate kubeconfig files for each EKS cluster associated with the SSO profiles found in the AWS configuration file.

## Output

The script generates kubeconfig files for each EKS cluster, named `<cluster-name>.yaml`. These files are created in the same directory as the script.

The generated kubeconfig files have the following properties:

- File permissions are set to 600 (read and write access for the owner only).
- The file owner is set to the current user running the script.

## Troubleshooting

If the script encounters any issues, such as access errors or failures in creating kubeconfig files, it will display appropriate error messages in the console.

## Notes

- The script assumes that you have the necessary permissions to list EKS clusters and generate kubeconfig files for the SSO profiles.
- The script uses the `aws eks update-kubeconfig` command to generate the kubeconfig files. Make sure you have the AWS CLI installed and configured correctly.
- The generated kubeconfig files are specific to the EKS clusters and SSO profiles at the time of running the script. If there are any changes to the clusters or profiles, you may need to re-run the script to update the kubeconfig files.

For any further questions or issues, please contact the script maintainer.
