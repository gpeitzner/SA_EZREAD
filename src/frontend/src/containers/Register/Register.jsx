
import * as React from 'react'
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Link from '@material-ui/core/Link';
import RadioGroup  from '@material-ui/core/RadioGroup';
import Radio  from '@material-ui/core/Radio';
import FormControlLabel  from '@material-ui/core/FormControlLabel';
import FormLabel  from '@material-ui/core/FormLabel';
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
    userTypeContainer: {
      marginTop: theme.spacing(2),
    }
  }));

const UserForm = () => {
    const classes = useStyles();

    return(
        <form className={classes.form} >
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="name"
                label="Nombre"
                name="name"
                autoComplete="name"
                autoFocus
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="lastname"
                label="Apellido"
                name="lastname"
                autoComplete="lastname"
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="phone"
                label="Telefono"
                name="phone"
                autoComplete="phone"
            />
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
                  Crear cuenta
                </Button>
          </form>
    )
}


const PublisherForm = () => {
    const classes = useStyles();

    return(
        <form className={classes.form} >
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="name"
                label="Nombre"
                name="name"
                autoComplete="name"
                autoFocus
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="address"
                label="Direccion"
                name="address"
                autoComplete="address"
            />
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
                  Crear cuenta
                </Button>
          </form>
    )
}


const Register = () =>  {
    const classes = useStyles();
    const [userType, setUserType] = React.useState('user')

    const handleChangeUserType = (event, value) => {
        setUserType(value)
    }
    return (
      <Container maxWidth="xs">
        <div className={classes.paper}>
            <Typography component="h1" variant="h5">
                Registro
            </Typography>
            <div className={classes.userTypeContainer}>
            <FormLabel component="legend">Quiero registrarme como:</FormLabel>
            <RadioGroup row aria-label="userType" name="userType" value={userType} onChange={handleChangeUserType}>
                <FormControlLabel value="user" control={<Radio />} label="Usuario" />
                <FormControlLabel value="publisher" control={<Radio />} label="Editorial" />
            </RadioGroup>
            </div>

            {
                userType === "user" && (
                    <UserForm />
                )
            }
            {
                userType === "publisher" && (
                    <PublisherForm />
                )
            }
            <Grid container>
                <Link href="/login" variant="body2">
                  {"Regresar a login"}
                </Link>
            </Grid>
        </div>
  
      </Container>
    );
  }

  export default Register