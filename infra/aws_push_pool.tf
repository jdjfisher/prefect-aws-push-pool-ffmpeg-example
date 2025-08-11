
variable "aws_access_key_id" {
  description = "The AWS access key ID"
  type        = string
}

variable "aws_secret_access_key" {
  description = "The AWS secret access key"
  type        = string
}

provider "aws" {
  region     = "eu-west-2"
  access_key = var.aws_access_key_id
  secret_key = var.aws_secret_access_key
}

resource "aws_iam_user" "prefect-ecs-user" {
  name = "prefect-ecs-user"
}

resource "aws_iam_user_policy" "prefect-ecs-policy" {
  name = "prefect-ecs-policy"
  user = aws_iam_user.prefect-ecs-user.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ecs:DescribeClusters",
          "ecs:ListClusters",
          "ecs:RegisterTaskDefinition",
          "ecs:DeregisterTaskDefinition",
          "ecs:ListTaskDefinitions",
          "ecs:RunTask",
          "ecs:StopTask",
          "ecs:DescribeTasks",
          "ecs:ListTasks",
        ]
        Resource = "*"
      },
    ]
  })
}

resource "aws_iam_access_key" "prefect-ecs-access-key" {
  user = aws_iam_user.prefect-ecs-user.name

}

resource "aws_ecr_repository" "prefect-ecs-repo" {
  name         = "prefect-flows"
  force_delete = true
}

resource "aws_ecs_cluster" "prefect-ecs-cluster" {
  name = "prefect-ecs-cluster"
}
