import os
import sys
import click
from flask import Flask, render_template
from flask import escape, url_for
from flask import request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

# app实例
app = Flask(__name__)

from tempwebserver import commands