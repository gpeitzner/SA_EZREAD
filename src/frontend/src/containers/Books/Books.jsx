import { Card, CardActionArea, CardActions, CardContent, CardMedia, IconButton, Typography } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles';
import * as React from 'react'
import AddCircleIcon from '@material-ui/icons/AddCircle';
import RemoveCircleIcon from '@material-ui/icons/RemoveCircle';

const books = [
    {
        "Editorial": "Espasa",
         "Titulo": "La Rebelión de las masas",
         "Genero": "Filosofía",
         "Autor" : "José Ortega y Gasset",
         "Activo": 1,
         "Cantidad" : 25,
         "id" :"60c0645b5a6ff4fc067a6bd3",
         "image":"https://enlinea.santotomas.cl/wp-content/uploads/sites/2/2020/10/Perros-mestizos.jpg"
         }
     
]

const useStyles = makeStyles((theme) => ({
    card: {
        maxWidth: "345px"
    },
    cardMedia: {
        height: 140
    },
    cardActions:{
        display: 'flex',
        justifyContent: 'space-between',
        paddingLeft: 90,
        paddingRight: 90,
    }
}))




const Books = () => {
    const classes = useStyles()
    
    const selectBook = (bookId) => {

    }

    
    return(
        <div>
        {
            books.map( book => (
                <Card key={book.id} className={classes.card}>
                    <CardActionArea onClick={ () => selectBook(book.id)}>
                        <CardMedia
                        className={classes.cardMedia}
                        image={book.image}
                        title={book.Title}
                        />
                        <CardContent>
                            <Typography gutterBottom variant="h5" component="h2">
                                {book.Titulo}
                            </Typography>
                            <Typography variant="body2" color="textSecondary" component="p">
                                Autor: {book.Editorial}
                                <br/>
                                Editorial: {book.Editorial}
                                <br/>
                                Genero: {book.Genero}
                            </Typography>
                        </CardContent>
                    </CardActionArea>
                    <CardActions className={classes.cardActions}>
                        <IconButton  aria-label="aceptar">
                            <RemoveCircleIcon />
                        </IconButton>
                        <Typography variant="h5" component="p">
                            0
                        </Typography>
                        <IconButton  aria-label="aceptar">
                            <AddCircleIcon />
                        </IconButton>
                    </CardActions>
                </Card>
            ))
        }
        </div>
    )
}

export default Books