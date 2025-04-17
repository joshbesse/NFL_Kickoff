import streamlit as st
import pandas as pd
import altair as alt

def return_rate_chart(df):
    df["year"] = df["year"].astype(float)
    year_ticks = df["year"].astype(int).tolist()

    base = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("year:Q", title="Season", axis=alt.Axis(values=year_ticks, format="d")),
        y=alt.Y("return_rate:Q", title="Return Rate (%)"),
        tooltip=[
            alt.Tooltip("year:O", title="Season:"),
            alt.Tooltip("return_rate:Q", title="Return Rate (%):")
        ]
    )

    rule = alt.Chart(pd.DataFrame({"year": [2023.5]})).mark_rule(
        color="red",
        strokeDash=[8, 5]
    ).encode(
        x="year:Q"
    )

    chart = (base + rule).properties(
        title="Return Rate Over Time",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

def return_yds_chart(df):
    df["year"] = df["year"].astype(float)
    year_ticks = df["year"].astype(int).tolist()

    base = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("year:Q", title="Season", axis=alt.Axis(values=year_ticks, format="d")),
        y=alt.Y("return_avg:Q", title="Average Return Distance (Yds)"),
        tooltip=[
            alt.Tooltip("year:O", title="Season:"),
            alt.Tooltip("return_avg:Q", title="Return Distance (Yds):")
        ] 
    )

    rule = alt.Chart(pd.DataFrame({"year": [2023.5]})).mark_rule(
        color="red",
        strokeDash=[8, 5]
    ).encode(
        x="year:Q"
    )

    chart = (base + rule).properties(
        title="Average Return Distance Over Time",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

def touchback_rate_chart(df):
    df["year"] = df["year"].astype(float)
    year_ticks = df["year"].astype(int).tolist()

    base = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("year:Q", title="Season", axis=alt.Axis(values=year_ticks, format="d")),
        y=alt.Y("touchback_rate:Q", title="Touchback Rate (%)"),
        tooltip=[
            alt.Tooltip("year:O", title="Season:"),
            alt.Tooltip("touchback_rate:Q", title="Touchback Rate (%):")
        ]
    )

    rule = alt.Chart(pd.DataFrame({"year": [2023.5]})).mark_rule(
        color="red",
        strokeDash=[8, 5]
    ).encode(
        x="year:Q"
    )

    chart = (base + rule).properties(
        title="Touchback Rate Over Time",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

def return_tds_chart(df):
    df["year"] = df["year"].astype(float)
    year_ticks = df["year"].astype(int).tolist()

    base = alt.Chart(df).mark_bar().encode(
        x=alt.X("year:Q", title="Season", axis=alt.Axis(values=year_ticks, format="d")),
        y=alt.Y("return_tds:Q", title="Returned Touchdowns"),
        tooltip=[
            alt.Tooltip("year:O", title="Season:"),
            alt.Tooltip("return_tds:Q", title="Returned Touchdowns:")
        ]
    )

    rule = alt.Chart(pd.DataFrame({"year": [2023.5]})).mark_rule(
        color="red",
        strokeDash=[8, 5]
    ).encode(
        x="year:Q"
    )

    chart = (base + rule).properties(
        title="Number of Returned Touchdowns Over Time",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

def return_20yds_chart(df):
    df["year"] = df["year"].astype(float)
    year_ticks = df["year"].astype(int).tolist()

    base = alt.Chart(df).mark_bar().encode(
        x=alt.X("year:Q", title="Season", axis=alt.Axis(values=year_ticks, format="d")),
        y=alt.Y("return_20+:Q", title="20+ Yard Returns"),
        tooltip=[
            alt.Tooltip("year:O", title="Season:"),
            alt.Tooltip("return_20+:Q", title="20+ Yard Returns:")
        ]
    )

    rule = alt.Chart(pd.DataFrame({"year": [2023.5]})).mark_rule(
        color="red",
        strokeDash=[8, 5]
    ).encode(
        x="year:Q"
    )
    
    chart = (base + rule).properties(
        title="Number of 20+ Yard Returns Over Time",
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

def return_40yds_chart(df):
    df["year"] = df["year"].astype(float)
    year_ticks = df["year"].astype(int).tolist()

    base = alt.Chart(df).mark_bar().encode(
        x=alt.X("year:Q", title="Season", axis=alt.Axis(values=year_ticks, format="d")),
        y=alt.Y("return_40+:Q", title="40+ Yard Returns"),
        tooltip=[
            alt.Tooltip("year:O", title="Season:"),
            alt.Tooltip("return_40+:Q", title="40+ Yard Returns:")
        ]
    )

    rule = alt.Chart(pd.DataFrame({"year": [2023.5]})).mark_rule(
        color="red",
        strokeDash=[8, 5]
    ).encode(
        x="year:Q"
    )

    chart = (base + rule).properties(
        title="Number of 40+ Yard Returns Over Time",
        height=400
    )
    
    st.altair_chart(chart, use_container_width=True)

# set page configs
st.set_page_config(
    page_title="NFL Kickoff Analysis",
    page_icon="🏈",
    layout="wide"
)

# remove top white space
st.markdown("""
    <style>
        .block-container {
            padding-top: 2.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# title
st.title("NFL Kickoff Rule Change Analysis")

# rule change motivation and summary
with st.expander("Motivation & Rule Changes", expanded=False):
    st.subheader("Motivation")
    st.markdown("""
    To address the lowest kickoff return rate in NFL history during the 2023 season and an unacceptable injury rate on kickoffs, NFL clubs have approved the Dynamic Kickoff rule for the 2024 season.
    
    The new form of a free kick play is designed to:
    - Resemble a typical scrimmage play by aligning players on both teams closer together and restricting movement to reduce space and speed.
    - Promote more returns.
    """)

    st.subheader("Rule Changes")
    st.markdown("""
    The ball is kicked from the A35 yard line (same as current rule)

    Safety kicks would be from A20 yard line (same as current rule)
                
    Alignment:
    - All kicking team players other than the kicker will line up with one foot on the receiving team’s B40 yard line
        - Kicker cannot cross the 50-yard line until ball touches the ground or player in landing zone or end zone
        - The 10 kicking team players cannot move until the ball hits the ground or player in the landing zone or the end zone
    - The receiving team will line up as follows:
        - Setup Zone – a 5-yard area from the B35 to the B30 yard line where at least 9 receiving team players must line up
            - At least 7 players with foot on the B35 yard line (restraining line) with alignment requirements (outside numbers, numbers to hashes, and inside hashes)
            - Players not on the restraining line must be lined up in setup zone outside the hash marks
            - All players in the setup zone cannot move until the kick has hit the ground or a player in the landing zone or the end zone
        - A maximum of 2 returners may line up in the landing zone and can move at any time prior to, or during, the kick
                
    Landing Zone:
    - Landing zone is the area between the receiving team’s goal line and its 20-yard line.
    - Any kick that hits short of the landing zone – treated like kickoff out of bounds and ball spotted at B40 yard line; play would be blown dead as soon as kick lands short of the landing zone
    - Any kick that hits in the landing zone - must be returned
    - Any kick that hits in the landing zone and then goes into the end zone – must be returned or downed by receiving team – if downed then touchback to B20 yard line
    - Kick hits in end zone, stays inbounds - returned or downed – if downed then touchback to B30 yard line
    - Any kick that goes out of the back of the end zone (in the air or bounces) – touchback to B30 yard line

    Miscellaneous:
    - If conditions cause ball to fall off tee twice, then kicker will be allowed to use kicking stick to keep the ball in place. The closest covering official will pick up the stick immediately after the kick
    - Onside kick:
        - 4th quarter begins, the team trailing has the opportunity to declare an onside kick to the officials
        - Current onside kickoff rules would apply. If onside kick goes beyond the setup zone untouched, kicking team penalized for UNS; return team would start the drive at the A20 yard line
    - Penalties:
        - The setup zone and landing zone will not change with any penalties that carry over to kickoffs. Alignment of 10 kickoff team players and all receiving team players would not change – only the spot of the kick would move
        - Penalties on scoring plays will not carry over and will be taken on the Try
        - Penalties on the Try may carry over, and if they do, only the placement of the kicker will change
    - Safety Kick:
        - The kick will be from the 20-yard line, and the kicker will have the option to use a tee; the setup zone and the landing zone will not change
    """)

# set two column layout
c1, spacer, c2 = st.columns([1, 0.05, 1])

# graphs showing return data over time
with c1:
    t1, t2, t3, t4, t5, t6 = st.tabs(["Return Rate", "Return Distance", "Touchback Rate", "Return TDs", "20+ Yard Returns", "40+ Yard Returns"])

    with t1:
        df = pd.read_pickle("./data/avg_return_rate.pkl")
        return_rate_chart(df)
    with t2:
        df = pd.read_pickle("./data/avg_return_yds.pkl")
        return_yds_chart(df)
    with t3:
        df = pd.read_pickle("./data/avg_touchback_rate.pkl")
        touchback_rate_chart(df)
    with t4:
        df = pd.read_pickle("./data/returned_touchdowns.pkl")
        return_tds_chart(df)
    with t5:
        df = pd.read_pickle("./data/returned_20.pkl")
        return_20yds_chart(df)
    with t6:
        df = pd.read_pickle("./data/returned_40.pkl")
        return_40yds_chart(df)

# metrics comparing season before rule changes and season with rule changes
with c2:
    st.subheader("2023 vs 2024 Metrics")
    left_col, right_col = st.columns([1, 1])
    with left_col:
        st.metric("Return Rate", "33.2%", "11.1%", border=True)
        st.metric("Touchback Rate", "63.9%", "-8.7%", border=True)
        st.metric("20+ Yard Returns", "808", "419", border=True)
    with right_col:
        st.metric("Average Return Distance", "27.9 yds", "4.7 yds", border=True)
        st.metric("Returned Touchdowns", "7", "3", border=True)
        st.metric("40+ Yard Returns", "59", "35", border=True)

# divider
st.markdown("""
<hr style='border: 1px solid #ccc; margin: 10px 0;' />
""", unsafe_allow_html=True)

st.subheader("Commentary & External Sources")
c3, c4, c5 = st.columns([1, 1, 1])
with c3:
    st.markdown("**[Concussions decrease to historic low in 2024 NFL season](https://www.nfl.com/news/concussions-decrease-historic-low-2024-dynamic-kickoff-lex-hip-drop-tackle)**")
    st.write("> The new rule slowed the average player speeds, as intended, which led to a lower concussion rate (down 43% vs. 2021-23 average) and the fewest lower extremity strains on the play since at least 2018.")
    st.write("> The Dynamic Kickoff rule also contributed to the lower extremity injury savings. Shorter distances and fewer high-speed efforts reduced the incidence of lower extremity strains by 48% on that play alone.")
with c4:
    st.markdown("**[NFL: Injury rate on kickoffs has dropped, similar to rate on plays from scrimmage](https://sports.yahoo.com/nfl-injury-rate-kickoffs-dropped-194930836.html)**")
    st.write("> On Wednesday, NFL executive vice president Jeff Miller provided an update on the injury numbers. While speaking to reporters at Wednesday's league meetings, Miller said that concussions and overall injuries are down across the board this season and that the injury rate on kickoffs has dropped to the point that it resembles the rate on plays from scrimmage. The NFL adopted the dynamic kickoff rule for the 2024 season only, but the results would seem to point toward its continued place in the game.")
with c5:
    st.markdown("**[https://x.com/SeifertESPN/status/1885063695308341757](https://x.com/SeifertESPN/status/1885063695308341757)**")
    st.write("> NFL said today that the injury rate on the new kickoff was the same as on other plays from scrimmage. Historically the injury rates on kickoffs has been 2-4 times that of all other plays. Concussion rate on kickoffs dropped 43%, per NFL's Jeff Miller.")
