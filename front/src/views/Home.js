import React, { useEffect, useState } from "react";

import { makeStyles } from "@material-ui/core/styles";
import {
  Grid,
  Paper,
  Divider,
  ListItem,
  List,
  ListItemIcon,
} from "@material-ui/core";

import BeachAccessIcon from "@material-ui/icons/BeachAccess";
import PeopleAltRoundedIcon from "@material-ui/icons/PeopleAltRounded";
import { useStyles } from "../components/styles";
// hoge
const Home = (props) => {
  const styles = useStyles();
  const [data, setData] = useState();
  useEffect(() => {
    fetch(process.env.REACT_APP_PUBLIC_URL + "/api/get_status", {
      mode: "cors",
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.length > 1) {
          setData([...data].sort((a, b) => a.updated_at - b.updated_at));
        }
        setData(data[0]);
      });
  }, []);
  return (
    <Grid container spacing={3} className={styles.root}>
      <Grid item xs={12}>
        <Paper className={styles.paper} elevation={3}>
          <h1>渋谷の状況</h1>
          <List style={{ margin: "3em" }}>
            <ListItem
              button
              onClick={() => {
                props.history.push("/weather");
              }}
            >
              <div className={styles.item}>
                <div className={styles.item2}>
                  <h2 className={styles.inneritem}>
                    <ListItemIcon>
                      <BeachAccessIcon color="primary" fontSize="large" />
                    </ListItemIcon>
                    天気　　{/*傘は大丈夫そう*/}約{data ? data.umbrella : null}
                    人
                  </h2>
                </div>
              </div>
            </ListItem>
            <Divider variant="inset" />
            <ListItem
              button
              onClick={() => {
                props.history.push("/crowd");
              }}
            >
              <div className={styles.item}>
                <div className={styles.item2}>
                  <h2 className={styles.inneritem}>
                    <ListItemIcon>
                      <PeopleAltRoundedIcon color="primary" fontSize="large" />
                    </ListItemIcon>
                    混雑　　約{data ? data.person : null}人
                  </h2>
                </div>
              </div>
            </ListItem>
            <ListItem>
              <div className={styles.item}>
                <div className={styles.item}>
                  {data ? data.updated_at : null}
                </div>
              </div>
            </ListItem>
          </List>
        </Paper>
      </Grid>
    </Grid>
  );
};
export default Home;
