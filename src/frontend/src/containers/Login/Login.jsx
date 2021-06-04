
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    paper: {
      marginTop: theme.spacing(8),
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    },
    avatar: {
      margin: theme.spacing(1),
      backgroundColor: theme.palette.secondary.main,
    },
    form: {
      width: '100%', // Fix IE 11 issue.
      marginTop: theme.spacing(1),
    },
    submit: {
      margin: theme.spacing(3, 0, 2),
    },
  }));


const Login = () =>  {
    const classes = useStyles();
    return (
      <Container maxWidth="xs">
        <div className={classes.paper}>
          <Typography component="h1" variant="h5">
              Login
          </Typography>
          <form className={classes.form} >
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="email"
                label="Correo"
                name="email"
                autoComplete="email"
                autoFocus
              />
              <TextField
                  variant="outlined"
                  margin="normal"
                  required
                  fullWidth
                  id="password"
                  label="Contraseña"
                  name="password"
                  autoComplete="password"
                  type="password"
                />
                <Button
                  type="submit"
                  fullWidth
                  variant="contained"
                  color="primary"
                  className={classes.submit}
                >
                  Login
                </Button>
  
            <Grid container>
                <Link href="/register" variant="body2">
                  {"Crea tu cuenta"}
                </Link>
            </Grid>
          </form>
        </div>
  
      </Container>
    );
  }

  export default Login