import React from "react";
import { Link } from "react-router-dom";
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
const Weather = () => {
  const styles = useStyles();
  return (
    <Grid container spacing={3} className={styles.root}>
      <Grid item xs={12}>
        <Paper className={styles.paper} elevation={3}>
          {/* <Link to="/"><img loop="infinite" border="0" src={Weathergif} alt="weather detection" /></Link> */}
        </Paper>
      </Grid>
    </Grid>
  );
};

export default Weather;
