import { makeStyles } from "@material-ui/core/styles";

export const useStyles = makeStyles((theme) => ({
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