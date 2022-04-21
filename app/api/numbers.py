from flask import Flask, render_template, request, redirect, flash, url_for, session, jsonify
from .. import app

@app.route("/print_numbers", methods=["GET"])
def print_numbers():
    app.logger.info("Print numbers from 1 to 100")
    numbers = []
    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            numbers.append("ThreeFive")
        elif number % 3 == 0:
            numbers.append("Three")
        elif number % 5 == 0:
            numbers.append("Five")
        else:
            numbers.append(number)
    return jsonify({"numbers": numbers})