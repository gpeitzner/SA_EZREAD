import { Container, FormGroup, TextField, Typography, Button, makeStyles, Select, MenuItem } from '@material-ui/core'
import * as React from 'react'
import { useFormik } from 'formik';
import axios from 'axios'

const useStyles = makeStyles( theme => ({
    form: {
        paddingTop: 40,
        paddingBottom: 40,
    },
    buttoContainer: {
        display: 'flex',
        paddingTop: 20,
        gap: 10
    },
    field: {
       paddingTop: 4,
       paddingBottom: 4,

    }
}))

const GET_URL=process.env.REACT_APP_REQUEST_COTIZADOR_URL


const RequestBook = () => {
    const classes = useStyles()
    const [impuestos, setImpuestos] = React.useState({})
    const [precio, setPrecio] = React.useState(0)
    const [impuesto, setImpuesto] = React.useState(0)

    React.useEffect(() => {
        const get  = async () => {
            const { data, status } = await axios.get(GET_URL)
            if(status === 200)
                setImpuestos(data.reduce((acc, value) => {
                    acc[value.pais] = value
                    return acc
                }, {}) )
        }
        get()
    }, [])




    return(
        <Container maxWidth="sm">
            <Typography component="h1" variant="h4">
                Cotizar libro
            </Typography>
            <Typography component="p" variant="subtitle1">
                Ingresa los datos de libro
            </Typography>
            <form className={classes.form} >
                <TextField
                fullWidth
                id="precio"
                name="precio"
                label="Precio"
                value={precio}
                type="number"
                onChange={(event) => setPrecio(event.target.value)}
                />
                <Select
                fullWidth
                id="impuesto"
                name="impuesto"
                label="Pais"
                value={impuesto}
                onChange={(event) => setImpuesto(event.target.value)}
                >
                    {
                    Object.keys(impuestos).map((key) => {
                        const obj = impuestos[key]
                        return(
                            <MenuItem value={obj.pais}>{obj.pais}</MenuItem>
                        )
                    })
                    }
                    
                    </Select>
                { 
                    precio && impuesto && (
                
                <div >
                <Typography component="h3" variant="h3">
                    {`El impuesto es de: ${impuestos[impuesto].impuesto.toFixed(2)}`}
                </Typography>
                    <Typography component="h3" variant="h3">
                        {`El total seria: ${((1+(impuestos[impuesto].impuesto/100)) * precio).toFixed(2)}`}
                    </Typography>
                </div>
                    )}
            </form>
        </Container>
    )
}

export default RequestBook