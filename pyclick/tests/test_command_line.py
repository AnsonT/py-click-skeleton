from unittest import TestCase
from click.testing import CliRunner
from pyclick.command_line import main
import click

class TestCommands(TestCase):
    def test_main(self):
        runner = CliRunner()
        result = runner.invoke(main)

    def test_test(self):
        runner = CliRunner()
        result = runner.invoke(main, ['test'])
