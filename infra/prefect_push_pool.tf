
variable "prefect_account_id" {
  description = "The Prefect account ID"
  type        = string
}

variable "prefect_workspace_id" {
  description = "The Prefect workspace ID"
  type        = string
}

variable "prefect_api_key" {
  description = "The Prefect API key"
  type        = string
}

provider "prefect" {
  api_key      = var.prefect_api_key
  account_id   = var.prefect_account_id
  workspace_id = var.prefect_workspace_id
}

resource "prefect_block" "aws_push_pool" {
  name      = "aws-push-pool"
  type_slug = "aws-credentials"
  data = jsonencode({
    "aws_access_key_id"     = aws_iam_access_key.prefect-ecs-access-key.id
    "aws_secret_access_key" = aws_iam_access_key.prefect-ecs-access-key.secret
    "region_name"           = "eu-west-2"
  })
}

resource "prefect_work_pool" "aws_push_pool" {
  name         = "aws-push-pool"
  type         = "aws_push"
  workspace_id = var.prefect_workspace_id
  base_job_template = jsonencode({
    job_configuration = {
      launch_type = "FARGATE"
      aws_credentials = {
        "$ref" = {
          block_document_id = prefect_block.aws_push_pool.id
        }
      }
    },
    variables = {}
  })
}
