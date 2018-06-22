from os.path import basename

import click
from click import argument, group, option, pass_context, pass_obj

from voximplant_client import VoximplantClient


@group()
@option('--account-id', type=click.STRING, required=True, help='Account id (or use VOXIMPLANT_ACCOUNT_ID env var)')
@option('--api-key', type=click.STRING, required=True, help='API key (use use VOXIMPLANT_API_KEY env var')
@pass_context
def cli(ctx, account_id, api_key):
    ctx.obj = VoximplantClient(account_id, api_key)


@cli.command(short_help='Upload the scenario file')
@argument('file', type=click.Path(exists=True))
@pass_obj
def upload(obj: VoximplantClient, file):
    with open(file, 'r') as f:
        result = obj.scenarios.add(
            name=basename(file),
            code=f.read(),
        )
        if not result.isError:
            print('OK')
        else:
            raise click.ClickException('Uploading error: {}'.format(result.error['msg']))


def main():
    return cli(
        obj=None,
        auto_envvar_prefix='VOXIMPLANT',
    )

if __name__ == '__main__':
    main()
