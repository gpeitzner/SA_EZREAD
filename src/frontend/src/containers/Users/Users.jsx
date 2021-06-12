import * as React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardContent, Container, IconButton, Typography } from '@material-ui/core';
import GroupAddIcon from '@material-ui/icons/GroupAdd';
import DeleteIcon from '@material-ui/icons/Delete';
import axios from 'axios'

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

const GET_URL = process.env.REACT_APP_USER_GET_ALL_URL
const UPDATE_URL = process.env.REACT_APP_USER_UPDATE_URL
const DELETE_URL = process.env.REACT_APP_USER_DELETE_URL

const Users = () => {
    const classes = useStyles()
    const [users, setUsers] = React.useState([])

    React.useEffect(() => {
        const getAsync = async () => {
            try {
              const { status, data } = await axios.get(GET_URL)
              if (status === 200) {
                  if(data.users)
                    setUsers(data.users)
              } else {
                  alert(data.message)
              }
            } catch(e) {
              alert('Login no exitoso')
            }
        }
        getAsync()
    }, [])

    const acceptUser = async (user) => {
        try {
            const values = {...user}
            values.activo = 1
            const { status, data } = await axios.post(UPDATE_URL, values)
            if (status === 200) {
                const tempUsers = users.map(u => {
                    if(u.id === values.id)
                        return values
                    return u
                })
                setUsers(tempUsers)
            } else {
                alert(data.message)
            }
          } catch(e) {
            alert('ha ocurrdio un error')
          }
    }

    const deleteUser = async (user) => {
        try {
            const values = {...user}
            user.activo = 1
            const { status, data } = await axios.delete(`${DELETE_URL}/${user.id}`, values)
            if (status === 200) {
                const tempUsers = users.filter( u => u.id !== user.id)
                setUsers(tempUsers)
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
                users.filter(user => user.tipo !== 'admin')
                .map(user => (
                    <Card className={classes.card}>
                        <CardContent className={classes.content}>
                            <Typography component="h5" variant="h5">
                                {`${user.nombre} ${user.apellido}`}
                            </Typography>
                            <Typography variant="subtitle1" color="textSecondary">
                                {user.correo}
                            </Typography>
                        </CardContent>
                        <div className={classes.controls}>
                            {
                                user.activo === "0" && (
                                    <IconButton onClick={() => acceptUser(user)} aria-label="aceptar">
                                        <GroupAddIcon />
                                    </IconButton>
                                )
                            }
                            <IconButton onClick={() => deleteUser(user)} aria-label="aceptar">
                                <DeleteIcon />
                            </IconButton>
                        </div>
                    </Card>
                ))
            }
        </Container>
    )
}

export default Users