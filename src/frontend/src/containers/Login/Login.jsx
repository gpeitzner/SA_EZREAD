
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import { useFormik } from 'formik'
import axios from 'axios'
import { useRecoilState } from 'recoil';
import { loginState } from '../../recoil/atoms';
import { useHistory } from 'react-router';

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

const CREATE_URL = process.env.REACT_APP_LOGIN_URL

const Login = () =>  {
    const classes = useStyles();
    const [login, setLogin] = useRecoilState(loginState)
    const history = useHistory()

    const formik = useFormik({
      initialValues: {
        email: '',
        password: ''

      },
      onSubmit: async (values, setSubmitting) => {
        try {
          const { status, data } = await axios.post(CREATE_URL, values)
          if (status === 200) {
            setLogin(data)
            history.push('/')
          } else {
              alert(data.message)
          }
        } catch(e) {
          alert('Login no exitoso')
        }

      },
    });

    return (
      <Container maxWidth="xs">
        <div className={classes.paper}>
          <Typography component="h1" variant="h5">
              Login
          </Typography>
          <form className={classes.form} onSubmit={formik.handleSubmit}>
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
                value={formik.values.email}
                onChange={formik.handleChange}
                error={formik.touched.email && Boolean(formik.errors.email)}
                helperText={formik.touched.email && formik.errors.email}
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