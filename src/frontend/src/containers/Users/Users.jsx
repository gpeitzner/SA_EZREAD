import * as React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardContent, Container, IconButton, Typography } from '@material-ui/core';
import GroupAddIcon from '@material-ui/icons/GroupAdd';
import DeleteIcon from '@material-ui/icons/Delete';

const users = [
    {
        "tipo":"user",
        "nombre":"pepito",
        "apellido":"perez",
        "correo": "pepito@gmail.com",
        "password":"123123",
        "telefono":"123123123",
        "direccion":"4av",
        "_id":"qweqweqwe"
    }
]

const useStyles = makeStyles((theme) => ({
    card: {
        display: 'flex'
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

const Users = () => {
    const classes = useStyles()

    const acceptUser = (userId) => {
        console.log(userId)
    }

    const deleteUser = (userId) => {
        console.log(userId)
    }

    return(
        <Container maxWidth="xs" className={classes.root}>
            {
                users.map(user => (
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
                            <IconButton onClick={() => acceptUser(user.id)} aria-label="aceptar">
                                <GroupAddIcon />
                            </IconButton>
                            <IconButton onClick={() => deleteUser(user.id)} aria-label="aceptar">
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