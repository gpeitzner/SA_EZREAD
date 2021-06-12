
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
import { useFormik } from 'formik';
import axios from 'axios';

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
    const formik = useFormik({
      initialValues: {
        tipo: 'usuario',
        nombre: '',
        apellido: '',
        correo: '',
        password: '',
        telefono: '',
        direccion: ''

      },
      onSubmit: async (values, setSubmitting) => {
        const { status, data } = await axios.post(CREATE_URL, values)
        if (status === 200) {
            alert(data.mensaje)
        } else {
            alert(data.message)
        }

      },
    });

    return(
        <form className={classes.form}   onSubmit={formik.handleSubmit}>
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="nombre"
                label="Nombre"
                name="nombre"
                autoComplete="name"
                autoFocus
                value={formik.values.nombre}
                onChange={formik.handleChange}
                error={formik.touched.nombre && Boolean(formik.errors.nombre)}
                helperText={formik.touched.nombre && formik.errors.nombre}
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="apellido"
                label="Apellido"
                name="apellido"
                autoComplete="lastname"
                value={formik.values.apellido}
                onChange={formik.handleChange}
                error={formik.touched.apellido && Boolean(formik.errors.apellido)}
                helperText={formik.touched.apellido && formik.errors.apellido}
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="telefono"
                label="Telefono"
                name="telefono"
                autoComplete="phone"
                value={formik.values.telefono}
                onChange={formik.handleChange}
                error={formik.touched.telefono && Boolean(formik.errors.telefono)}
                helperText={formik.touched.telefono && formik.errors.telefono}
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="correo"
                label="Correo"
                name="correo"
                autoComplete="correo"
                value={formik.values.correo}
                onChange={formik.handleChange}
                error={formik.touched.correo && Boolean(formik.errors.correo)}
                helperText={formik.touched.correo && formik.errors.correo}
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
                  value={formik.values.password}
                  onChange={formik.handleChange}
                  error={formik.touched.password && Boolean(formik.errors.password)}
                  helperText={formik.touched.password && formik.errors.password}
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

const CREATE_URL = process.env.REACT_APP_USER_CREATE_URL

const PublisherForm = () => {
    const classes = useStyles();

    const formik = useFormik({
      initialValues: {
        tipo: 'editor',
        nombre: '',
        apellido: '',
        correo: '',
        password: '',
        telefono: '',
        direccion: ''

      },
      onSubmit: async (values, setSubmitting) => {
        const { status, data } = await axios.post(CREATE_URL, values)
        if (status === 200) {
            alert(data.mensaje)
        } else {
            alert(data.message)
        }

      },
    });

    return(
        <form className={classes.form}  onSubmit={formik.handleSubmit}>
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="nombre"
                label="Nombre"
                name="nombre"
                autoComplete="name"
                autoFocus
                value={formik.values.nombre}
                onChange={formik.handleChange}
                error={formik.touched.nombre && Boolean(formik.errors.nombre)}
                helperText={formik.touched.nombre && formik.errors.nombre}
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="direccion"
                label="Direccion"
                name="direccion"
                autoComplete="address"
                value={formik.values.direccion}
                onChange={formik.handleChange}
                error={formik.touched.direccion && Boolean(formik.errors.direccion)}
                helperText={formik.touched.direccion && formik.errors.direccion}
            />
            <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="correo"
                label="Correo"
                name="correo"
                autoComplete="email"
                autoFocus
                value={formik.values.correo}
                onChange={formik.handleChange}
                error={formik.touched.correo && Boolean(formik.errors.correo)}
                helperText={formik.touched.correo && formik.errors.correo}
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
                  value={formik.values.password}
                  onChange={formik.handleChange}
                  error={formik.touched.password && Boolean(formik.errors.password)}
                  helperText={formik.touched.password && formik.errors.password}
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