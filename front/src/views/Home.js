import React from "react";
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

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: "center",
    color: theme.palette.text.secondary,
  },
  item: {
    margin: "0 auto",
  },
  item2: {
    width: "335px",
    textAlign: "left",
  },
  inneritem: {
    display: "flex",
  },
}));

const Home = (props) => {
  const styles = useStyles();
  //   console.log(props);
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
                    天気　　傘は大丈夫そう
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
                    混雑　　20/100
                  </h2>
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
