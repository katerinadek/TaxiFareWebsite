from altair.vegalite.v4.schema.channels import Latitude
import streamlit as st
import datetime
from numpy.core.arrayprint import DatetimeFormat
import pandas as pd
import requests

st.markdown(
    f"TaxiFareModel"
)

departure_date = st.date_input('Date:',
        datetime.datetime.today()
        )

departure_time = st.time_input('Departure', datetime.time(8, 45)
)

passenger_count = st.number_input('Passengers:', 1, format ='%i')

#st.write(f'Departing on {departure_date} at {departure_time}')


plon = st.text_input('Pickup longitude:')
plat =st.text_input('Pickup latitude:')
dlon =st.text_input('Dropoff longitude:')
dlat=st.text_input('Dropoff latitude:')

url='https://taxifare.lewagon.ai/predict'

formatted_pickup_datetime=datetime.datetime.combine(departure_date, departure_time)

X_pred = {
    'pickup_datetime': formatted_pickup_datetime,
    'pickup_longitude': float(plon),
    'pickup_latitude': float(plat),
    'dropoff_longitude': float(dlon),
    'dropoff_latitude': float(dlat),
    'passenger_count': passenger_count
}

df = pd.DataFrame({'lon': [float(plon),float(dlon)],
            'lat':[float(plat), float(dlat)]
            })

st.write(df)

#st.write(X_pred)
prediction = requests.get(url, params=X_pred).json()

st.write(prediction)

st.map(df)