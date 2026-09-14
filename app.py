from flask import Flask, request, render_template_string, send_from_directory
import model2
import os

app = Flask(__name__)


# ---------------- IMAGE ROUTE ----------------

@app.route("/villa_bg.png")
def villa_bg():
    return send_from_directory(
        os.path.dirname(os.path.abspath(__file__)),
        "villa_bg.png"
    )


# ---------------- HTML + CSS ----------------

HTML = """
<!DOCTYPE html>
<html>

<head>

    <title>HOUSE | Price Prediction</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, sans-serif;
            background: #071426;
            color: white;
            overflow: hidden;
        }

        .page {
            min-height: 100vh;
            display: flex;
        }


        /* ================= LEFT ================= */

        .left {
            width: 48%;
            min-height: 100vh;
            padding: 45px 5%;
            background: linear-gradient(
                135deg,
                #071426,
                #10294a
            );

            display: flex;
            flex-direction: column;
            justify-content: center;

            position: relative;
            z-index: 2;
        }

        .title {
            font-size: 58px;
            font-weight: bold;
            letter-spacing: 7px;
            margin: 0;
            animation: slide 0.8s ease;
        }

        .subtitle {
            color: #a9bdd8;
            font-size: 20px;
            margin: 8px 0 28px;
            animation: slide 1s ease;
        }


        /* ================= FORM ================= */

        .form {
            width: 100%;
            max-width: 520px;

            background: rgba(255,255,255,0.08);

            padding: 22px;

            border-radius: 20px;

            border: 1px solid rgba(255,255,255,0.18);

            backdrop-filter: blur(12px);

            animation: up 0.9s ease;
        }

        .row {
            display: flex;
            gap: 15px;
            margin-bottom: 3px;
        }

        .field {
            flex: 1;
            min-width: 0;
        }

        label {
            display: block;
            margin: 7px 0;

            color: #cbd5e1;

            font-size: 14px;
        }

        input {
            width: 100%;

            padding: 12px;

            border: 1px solid #426184;

            border-radius: 10px;

            background: rgba(255,255,255,0.08);

            color: white;

            outline: none;

            font-size: 14px;

            transition: 0.3s;
        }

        input:focus {
            border-color: #38bdf8;

            box-shadow:
                0 0 12px rgba(56,189,248,0.3);

            transform: scale(1.01);
        }

        input::placeholder {
            color: #8fa6c2;
        }


        /* ================= BUTTON ================= */

        button {
            width: 100%;

            margin-top: 15px;

            padding: 14px;

            border: none;

            border-radius: 10px;

            background:
                linear-gradient(
                    90deg,
                    #1683ff,
                    #8146ff
                );

            color: white;

            font-size: 17px;

            font-weight: bold;

            cursor: pointer;

            transition: 0.3s;

            box-shadow:
                0 5px 15px rgba(80,100,255,0.2);
        }

        button:hover {
            transform: translateY(-3px);

            box-shadow:
                0 10px 25px rgba(80,100,255,0.45);
        }


        /* ================= RESULT ================= */

        .result {
            margin-top: 16px;

            padding: 15px;

            border-radius: 12px;

            background: rgba(0,200,130,0.12);

            border: 1px solid #00c98a;

            animation: pop 0.5s ease;
        }

        .price {
            color: #55f2ad;

            font-size: 27px;

            font-weight: bold;

            margin-top: 5px;
        }

        .error {
            color: #ff6b6b;

            margin-top: 12px;

            font-size: 14px;
        }


        /* ================= RIGHT VILLA ================= */

        .villa {
            width: 52%;

            min-height: 100vh;

            position: relative;

            overflow: hidden;

            background: #071426;
        }

        .villa img {
            width: 125%;
            height: 100%;

            object-fit: cover;

            object-position: right center;

            display: block;

            position: absolute;

            right: 0;
            top: 0;

            animation: villaZoom 1.5s ease;
        }

        .villa::after {
            content: "";

            position: absolute;

            inset: 0;

            background:
                linear-gradient(
                    90deg,
                    rgba(7,20,38,0.18),
                    transparent 40%
                );
        }


        /* ================= VILLA TEXT ================= */

        .villa-text {
            position: absolute;

            bottom: 40px;

            right: 35px;

            z-index: 2;

            font-size: 26px;

            font-style: italic;

            text-align: right;

            text-shadow:
                0 3px 15px black;

            animation: up 1.3s ease;
        }


        /* ================= ANIMATIONS ================= */

        @keyframes slide {

            from {
                opacity: 0;
                transform: translateX(-40px);
            }

            to {
                opacity: 1;
                transform: translateX(0);
            }

        }


        @keyframes up {

            from {
                opacity: 0;
                transform: translateY(35px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }

        }


        @keyframes pop {

            from {
                opacity: 0;
                transform: scale(0.9);
            }

            to {
                opacity: 1;
                transform: scale(1);
            }

        }


        @keyframes villaZoom {

            from {
                opacity: 0;
                transform: scale(1.08);
            }

            to {
                opacity: 1;
                transform: scale(1);
            }

        }


        /* ================= MOBILE ================= */

        @media(max-width: 900px) {

            body {
                overflow: auto;
            }

            .page {
                display: block;
            }

            .left {
                width: 100%;
                min-height: auto;
                padding: 35px 25px;
            }

            .villa {
                width: 100%;
                height: 400px;
                min-height: 400px;
            }

            .title {
                font-size: 42px;
            }

            .row {
                flex-direction: column;
                gap: 0;
            }

            .villa img {
                width: 100%;
            }

        }

    </style>

</head>


<body>


<div class="page">


    <!-- ================= LEFT ================= -->

    <div class="left">

        <h1 class="title">
            HOUSE
        </h1>

        <div class="subtitle">
            Price Prediction
        </div>


        <form method="POST" class="form">


            <!-- AREA + BEDROOMS -->

            <div class="row">

                <div class="field">

                    <label>
                        Area (sq ft)
                    </label>

                    <input
                        type="number"
                        name="area"
                        placeholder="e.g. 1500"
                        required
                    >

                </div>


                <div class="field">

                    <label>
                        Bedrooms
                    </label>

                    <input
                        type="number"
                        name="bedrooms"
                        placeholder="e.g. 3"
                        required
                    >

                </div>

            </div>


            <!-- BATHROOM + AGE -->

            <div class="row">

                <div class="field">

                    <label>
                        Bathrooms
                    </label>

                    <input
                        type="number"
                        name="bathrooms"
                        placeholder="e.g. 2"
                        required
                    >

                </div>


                <div class="field">

                    <label>
                        House Age
                    </label>

                    <input
                        type="number"
                        name="house_age"
                        placeholder="e.g. 5"
                        required
                    >

                </div>

            </div>


            <!-- DISTANCE + LOCATION SCORE -->

            <div class="row">

                <div class="field">

                    <label>
                        Distance
                    </label>

                    <input
                        type="number"
                        name="distance"
                        placeholder="e.g. 5"
                        required
                    >

                </div>


                <div class="field">

                    <label>
                        Location Score
                    </label>

                    <input
                        type="number"
                        name="location_score"
                        placeholder="e.g. 2"
                        required
                    >

                </div>

            </div>


            <!-- BUTTON -->

            <button type="submit">

                ✨ Predict Price →

            </button>


            <!-- RESULT -->

            {% if prediction is not none %}

            <div class="result">

                Estimated House Price

                <div class="price">

                    ₹ {{ "%.2f"|format(prediction) }} Lakhs

                </div>

            </div>

            {% endif %}


            <!-- ERROR -->

            {% if error %}

            <div class="error">

                ⚠ {{ error }}

            </div>

            {% endif %}


        </form>

    </div>



    <!-- ================= RIGHT ================= -->

    <div class="villa">

        <img
            src="/villa_bg.png"
            alt="Luxury Villa"
        >

        <div class="villa-text">

            Better Homes,<br>
            Brighter Future

        </div>

    </div>


</div>


</body>

</html>
"""


# ---------------- HOME ROUTE ----------------

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    error = None

    if request.method == "POST":

        try:

            data = [[

                int(request.form["area"]),

                int(request.form["bedrooms"]),

                int(request.form["bathrooms"]),

                int(request.form["house_age"]),

                int(request.form["distance"]),

                int(request.form["location_score"])

            ]]

            prediction = model2.model.predict(data)[0]

        except Exception as e:

            error = str(e)

    return render_template_string(
        HTML,
        prediction=prediction,
        error=error
    )


# ---------------- RUN APP ----------------

if __name__ == "__main__":

    app.run(debug=True)