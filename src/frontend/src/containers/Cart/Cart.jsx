import * as React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardContent, Container, IconButton, Typography, CardMedia,CardActions,FormLabel,RadioGroup,Radio,FormControlLabel,Button } from '@material-ui/core';
import { useRecoilState } from 'recoil';
import { cartState,loginState } from '../../recoil/atoms';
import AddCircleIcon from '@material-ui/icons/AddCircle';
import RemoveCircleIcon from '@material-ui/icons/RemoveCircle';
import axios from 'axios'


const useStyles = makeStyles((theme) => ({
    card: {
        display: 'flex'
    },
    root: {
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gridColumnGap: 20
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
  cardMedia: {
      width: 200
  }
}))


const CREATE_URL = process.env.REACT_APP_ORDER_CREATE_URL

console.log({CREATE_URL})

const Cart = () => {

    const [cart, setCart] = useRecoilState(cartState)
    const [paymentType, setPaymentType] = React.useState('tarjeta')
    const [shippingType, setShippingTypeType] = React.useState('normal')
    const [login] = useRecoilState(loginState)
    const classes = useStyles()

    const addToCart = (book,quantity) => {
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

    const handleChangePaymentType = (event, value) => {
        setPaymentType(value)
    }

    const handleChangeShippingType = (event, value) => {
        setShippingTypeType(value)

    }

    const createOrder = async () => {
        const values = {
            usuario: login._id,
            tipoPago: paymentType,
            tipoEnvio: shippingType,
            nombreUsuario: login.nombre,
            correoUsuario: login.correo,
            libros: Object.keys(cart).map(key => {
                const book = { ...cart[key] }
                return {
                    id: book.id,
                    cantidad: `${book.quantity}`,
                    precio: `${book.Precio}`,
                }
            })
        }
        console.log({values, login})
        const { status, data } = await axios.post(CREATE_URL, values)
        if (status === 200) {
            alert(data.mensaje)
        } else {
        alert(data.message)
        }
    }

    return(
        <Container className={classes.root}>
            <div>
            {
                Object.keys(cart).map(key => {
                    const book = cart[key]
                    return (
                    <Card className={classes.card}>
                        <CardMedia
                        className={classes.cardMedia}
                        image={book.Imagen}
                        title={book.Title}
                        />
                        <CardContent className={classes.content}>
                            <Typography component="h5" variant="h5">
                                {book.Titulo}
                            </Typography>
                            <Typography variant="subtitle1" color="textSecondary">
                                {book.Editorial}
                            </Typography>
                        </CardContent>
                        <div className={classes.controls}>
                        <CardActions className={classes.cardActions}>
                            <IconButton  aria-label="aceptar" onClick={() => addToCart(book,-1)}>
                                <RemoveCircleIcon />
                            </IconButton>
                            <Typography variant="h5" component="p">
                                { cart[book.id] ? cart[book.id].quantity : '0'}
                            </Typography>
                            <IconButton  aria-label="aceptar" onClick={() => addToCart(book,1)}>
                                <AddCircleIcon />
                            </IconButton>
                        </CardActions>
                        </div>
                    </Card>
                )})
            }</div>
            <div>
                <Typography component="h3" variant="h5">
                    Termina tu compra
                </Typography>

            <FormLabel component="legend">Forma de Pago:</FormLabel>
            <RadioGroup row aria-label="paymentType" name="paymentType" value={paymentType} onChange={handleChangePaymentType}>
                <FormControlLabel value="efectivo" control={<Radio />} label="Efectivo" />
                <FormControlLabel value="tarjeta" control={<Radio />} label="Tarjeta" />
            </RadioGroup>
            <FormLabel component="legend">Tipo de envio:</FormLabel>
            <RadioGroup row aria-label="shippingType" name="shippingType" value={shippingType} onChange={handleChangeShippingType}>
                <FormControlLabel value="express" control={<Radio />} label="Express" />
                <FormControlLabel value="normal" control={<Radio />} label="Normal" />
            </RadioGroup>

            <br/>
            <Button color="primary" variant="contained" fullWidth type="button" onClick={createOrder}>
                Comprar
            </Button>
            </div>
        </Container>
    )
}

export default Cart