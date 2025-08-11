terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92"
    }

    prefect = {
      source  = "prefecthq/prefect"
      version = "~> 2.84"
    }
  }

  required_version = ">= 1.2"
}
