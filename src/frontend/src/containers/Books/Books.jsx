import { Card, CardActionArea, CardActions, CardContent, CardMedia, IconButton, Typography } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles';
import * as React from 'react'
import AddCircleIcon from '@material-ui/icons/AddCircle';
import RemoveCircleIcon from '@material-ui/icons/RemoveCircle';
import { useRecoilState } from 'recoil';
import { cartState } from '../../recoil/atoms';
import axios from 'axios';

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
         },
         {
             "Editorial": "Espasa",
              "Titulo": "La Rebelión de las masas",
              "Genero": "Filosofía",
              "Autor" : "José Ortega y Gasset",
              "Activo": 1,
              "Cantidad" : 0,
              "id" :"60c0645b5a6ff4fc067a6bdee",
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

const Book = ({book}) => {

    const [cart, setCart] = useRecoilState(cartState)
    
    const selectBook = (bookId) => {

    }

    const addToCart = (quantity) => {
        const tempCart = { ...cart}

        if (tempCart[book.id]) {
            const tempProd = { ...tempCart[book.id] }
            if (tempProd.quantity) {
            tempProd.quantity = tempProd.quantity + quantity
            if (tempProd.quantity > 0) {
                tempCart[book.id] = {
                ...tempProd
                }
                setCart(tempCart)
            } else {
                delete tempCart[book.id]
            }
            }
        } else if (quantity > 0) {
            tempCart[book.id] = {
            ...book,
            quantity,
            }
        }

        setCart(tempCart)
    }


    const classes = useStyles()

    return (
        <Card className={classes.card}>
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
                <IconButton  aria-label="aceptar" onClick={() => addToCart(-1)}>
                    <RemoveCircleIcon />
                </IconButton>
                <Typography variant="h5" component="p">
                    { cart[book.id] ? cart[book.id].quantity : '0'}
                </Typography>
                <IconButton  aria-label="aceptar" onClick={() => addToCart(1)}>
                    <AddCircleIcon />
                </IconButton>
            </CardActions>
        </Card>
    )
}

const GET_URL = process.env.REACT_APP_BOOK_GET_ALL_URL


const Books = () => {
    const classes = useStyles()

    React.useEffect(() => {
        const getAsync = async () => {
                const { status, data } = await axios.get(`${GET_URL}`)
                if (status === 200) {
                    alert(data.mensaje)
                } else {
                    alert(data.message)
                }
        }
        getAsync()
    }, [])


    return(
        <div>
        {
            books.filter(book => book.Cantidad > 0 ).map( book => (
                <Book key={book.id}  book={book}/>
            ))
        }
        </div>
    )
}

export default Books