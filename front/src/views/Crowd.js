import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { Grid, Paper } from "@material-ui/core";

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
const Crowd = () => {
  const styles = useStyles();
  return (
    <Grid container spacing={3} className={styles.root}>
      <Grid item xs={12}>
        <Paper className={styles.paper} elevation={3}></Paper>
      </Grid>
    </Grid>
  );
};

export default Crowd;
