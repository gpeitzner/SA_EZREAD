import { Card, CardActionArea, CardActions, CardContent, CardMedia, IconButton, Typography } from '@material-ui/core'
import { Link } from 'react-router-dom'
import { makeStyles } from '@material-ui/core/styles';
import * as React from 'react'
import AddCircleIcon from '@material-ui/icons/AddCircle';
import RemoveCircleIcon from '@material-ui/icons/RemoveCircle';
import { useRecoilState } from 'recoil';
import { cartState } from '../../recoil/atoms';
import axios from 'axios';

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexWrap: 'wrap',
    },
    card: {
        maxWidth: "345px",
        margin: 10
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
                image={book.Imagen}
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
                    <Link to={`/books/${book.id}/edit`} >
                        Editar
                    </Link>
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
    const [libros, setLibros] = React.useState([])

    React.useEffect(() => {
        const getAsync = async () => {
                const { status, data } = await axios.get(`${GET_URL}`)
                if (status === 200) {
                    if(data && data.libros)
                        setLibros(data.libros)
                } else {
                    alert(data.message)
                }
        }
        getAsync()
    }, [])


    return(
        <div className={classes.root}>
        {
            libros.filter(book => book.Cantidad > 0 ).map( book => (
                <Book key={book.id}  book={book}/>
            ))
        }
        </div>
    )
}

export default Books