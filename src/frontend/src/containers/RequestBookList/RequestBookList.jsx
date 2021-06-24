import * as React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardContent, Container, IconButton, Typography } from '@material-ui/core';
import GroupAddIcon from '@material-ui/icons/GroupAdd';
import DeleteIcon from '@material-ui/icons/Delete';
import axios from 'axios'
import { useRecoilState } from 'recoil';
import { loginState } from '../../recoil/atoms';

const useStyles = makeStyles((theme) => ({
    card: {
        display: 'flex',
        marginBottom: 20,
    },
    root: {
        display: 'flex',
        flexDirection: 'column'
    },
    content: {
        flex: '2'
    },

  controls: {
    display: 'flex',
    alignItems: 'flexEnd',
    flex: '1',
    paddingLeft: theme.spacing(1),
    paddingBottom: theme.spacing(1),
  },
}))

const GET_URL = process.env.REACT_APP_REQUEST_GET_ALL_URL
const CREATE_URL = process.env.REACT_APP_BOOK_CREATE_URL



const RequestBookList = () => {
    const classes = useStyles()
    const [requests, setRequests] = React.useState([])
    const [login, setLogin] = useRecoilState(loginState)

    React.useEffect(() => {
        const getAsync = async () => {
            try {
              const { status, data } = await axios.get(GET_URL)
              if (status === 200) {
                  if(data)
                  setRequests(data)
              } else {
                  alert(data.message)
              }
            } catch(e) {
              alert('Login no exitoso')
            }
        }
        getAsync()
    }, [])

    console.log({requests})

    const acceptUser = async (request) => {
        try {
            const nValues = { 
                Imagen: '',
                Activo: 1,
                Autor: request.autor,
                Cantidad: 100,
                Editorial: login.nombre,
                Genero: "Ebook",
                Precio: 100,
                Titulo: request.nombre,
             }
            
            const { status, data } = await axios.post(CREATE_URL, nValues)

            if(status === 200) {
                const { status, data } = await axios.delete(`${GET_URL}?id=${request.id}`)
                if (status === 200) {
                    const tempUsers = requests.filter( u => u.id !== request.id)
                    setRequests(tempUsers)
                } else {
                    alert(data.message)
                }
            }
        } catch(e) {
        alert('ha ocurrdio un error')
        }
    }

    const deleteUser = async (request) => {
        try {
            const { status, data } = await axios.delete(`${GET_URL}?id=${request.id}`)
            if (status === 200) {
                const tempUsers = requests.filter( u => u.id !== request.id)
                setRequests(tempUsers)
            } else {
                alert(data.message)
            }
          } catch(e) {
            alert('ha ocurrdio un error')
          }
    }

    return(
        <Container maxWidth="xs" className={classes.root}>
            {
                requests.map(request => (
                    <Card className={classes.card}>
                        <CardContent className={classes.content}>
                            <Typography component="h5" variant="h5">
                                {request.nombre}
                            </Typography>
                            <Typography variant="subtitle1" color="textSecondary">
                                {`Autor: ${request.autor} - ${request.fecha}`}
                            </Typography>
                        </CardContent>
                        <div className={classes.controls}>
                            <IconButton onClick={() => acceptUser(request)} aria-label="aceptar">
                                <GroupAddIcon />
                            </IconButton>
                            <IconButton onClick={() => deleteUser(request)} aria-label="aceptar">
                                <DeleteIcon />
                            </IconButton>
                        </div>
                    </Card>
                ))
            }
        </Container>
    )
}

export default RequestBookList