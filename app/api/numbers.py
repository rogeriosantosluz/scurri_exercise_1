from flask import Flask, render_template, request, redirect, flash, url_for, session, jsonify
from .. import app

@app.route("/print_numbers", methods=["GET"])
def print_numbers():
    app.logger.info("Print numbers from 1 to 100")
    return "OK"