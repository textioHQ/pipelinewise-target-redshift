import os


def get_db_config():
    config = {"host": os.environ.get("TARGET_REDSHIFT_HOST")}

    config["port"] = os.environ.get("TARGET_REDSHIFT_PORT")
    config["user"] = os.environ.get("TARGET_REDSHIFT_USER")
    config["password"] = os.environ.get("TARGET_REDSHIFT_PASSWORD")
    config["dbname"] = os.environ.get("TARGET_REDSHIFT_DBNAME")
    config["default_target_schema"] = os.environ.get("TARGET_REDSHIFT_SCHEMA")

    # AWS IAM and S3 bucket
    config["aws_access_key_id"] = os.environ.get("TARGET_REDSHIFT_AWS_ACCESS_KEY")
    config["aws_secret_access_key"] = os.environ.get(
        "TARGET_REDSHIFT_AWS_SECRET_ACCESS_KEY"
    )
    config["s3_acl"] = os.environ.get("TARGET_REDSHIFT_S3_ACL")
    config["s3_bucket"] = os.environ.get("TARGET_REDSHIFT_S3_BUCKET")
    config["s3_key_prefix"] = os.environ.get("TARGET_REDSHIFT_S3_KEY_PREFIX")

    # --------------------------------------------------------------------------
    # The following variables needs to be empty.
    # The tests cases will set them automatically whenever it's needed
    # --------------------------------------------------------------------------
    config["disable_table_cache"] = None
    config["schema_mapping"] = None
    config["add_metadata_columns"] = None
    config["hard_delete"] = None
    config["aws_redshift_copy_role_arn"] = None
    config["flush_all_streams"] = None
    config["validate_records"] = None

    return config


def get_test_config():
    return get_db_config()


def get_test_tap_lines(filename):
    lines = []
    with open(f"{os.path.dirname(__file__)}/resources/{filename}") as tap_stdout:
        lines.extend(iter(tap_stdout))
    return lines
