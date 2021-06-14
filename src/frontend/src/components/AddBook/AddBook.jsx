import { Container, FormGroup, TextField, Typography, Button, makeStyles } from '@material-ui/core'
import * as React from 'react'
import { useFormik } from 'formik';
import axios from 'axios'
import { useParams } from 'react-router-dom'

const getBase64 = (file) => new Promise((resolve) => {
    // let fileInfo
    let baseURL = ''
    // Make new FileReader
    const reader = new FileReader()
  
    // Convert the file to base64 text
    reader.readAsDataURL(file)
  
    // on reader load somthing...
    reader.onload = () => {
      // Make a fileInfo Object
      baseURL = reader.result
      const c = baseURL.split(',')
      resolve(c[1])
    }
  })
  


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

const emptyBook = {
    "Editorial": "",
     "Titulo": "",
     "Genero": "",
     "Autor" : "",
     "Activo": 1,
     "Cantidad" : 0,
    // "Image":"https://enlinea.santotomas.cl/wp-content/uploads/sites/2/2020/10/Perros-mestizos.jpg"
}

const CREATE_URL = process.env.REACT_APP_BOOK_CREATE_URL
const GET_URL = process.env.REACT_APP_BOOK_GET_URL
const EDIT_URL = process.env.REACT_APP_BOOK_EDIT_URL
const DELETE_URL =  process.env.REACT_APP_BOOK_DELETE_URL

const AddBook = () => {
    const classes = useStyles()
    const { bookId } = useParams()
    const [libro, setLibro] = React.useState(null)
    const [fotografia, setFotografia] = React.useState("")

    console.log({bookId})
    

    React.useEffect(() => {
        const getAsync = async () => {
            if(bookId) {
                const { status, data } = await axios.get(`${GET_URL}?id=${bookId}`)
                if (status === 200) {
                    if(data && data.libro) {
                        setLibro({...data.libro, cambioFoto : false, fotografia: ''})
                        formik.setValues(data.libro)
                    }
                } else {
                    alert(data.message)
                }
            }
        }
        getAsync()
    }, [bookId])


    const deleteAction = async () => {
        const { status, data } = await axios.delete(`${DELETE_URL}?id=${bookId}`)
        if (status === 200) {
            alert(data.mensaje)
        } else {
            alert(data.message)
        }
    }

    const formik = useFormik({
        initialValues: {},
        onSubmit: async (values, setSubmitting) => {
            console.log({bookId})
            if(bookId) {
                const nValues = { ...values }
                if(fotografia) {
                    nValues.Imagen = fotografia
                }

                const { status, data } = await axios.put(`${EDIT_URL}`, nValues)
                if (status === 200) {
                    alert(data.mensaje)
                } else {
                  alert(data.message)
                }
                setSubmitting(false)
            } else {
                const nValues = { ...values, 
                    "Activo": 1 }
                if(fotografia) {
                    nValues.Imagen = fotografia
                }
                const { status, data } = await axios.post(CREATE_URL, nValues)
                if (status === 200) {
                    alert(data.mensaje)
                } else {
                alert(data.message)
                }
                setSubmitting(false)
            }
  
        },
      });


    return(
        <Container maxWidth="sm">
            <Typography component="h1" variant="h4">
                Libro
            </Typography>
            <Typography component="p" variant="subtitle1">
                Ingresa los datos de libro
            </Typography>
            <form className={classes.form} onSubmit={formik.handleSubmit}>
                <TextField
                fullWidth
                id="Titulo"
                name="Titulo"
                label="Titulo"
                value={formik.values.Titulo}
                onChange={formik.handleChange}
                error={formik.touched.Titulo && Boolean(formik.errors.Titulo)}
                helperText={formik.touched.Titulo && formik.errors.Titulo}
                className={classes.field}
                />
                <TextField
                fullWidth
                id="Editorial"
                name="Editorial"
                label="Editorial"
                value={formik.values.Editorial}
                onChange={formik.handleChange}
                error={formik.touched.Editorial && Boolean(formik.errors.Editorial)}
                helperText={formik.touched.Editorial && formik.errors.Editorial}
                className={classes.field}
                />
                <TextField
                fullWidth
                id="Genero"
                name="Genero"
                label="Genero"
                value={formik.values.Genero}
                onChange={formik.handleChange}
                error={formik.touched.Genero && Boolean(formik.errors.Genero)}
                helperText={formik.touched.Genero && formik.errors.Genero}
                className={classes.field}
                />
                <TextField
                fullWidth
                id="Autor"
                name="Autor"
                label="Autor"
                value={formik.values.Autor}
                onChange={formik.handleChange}
                error={formik.touched.Autor && Boolean(formik.errors.Autor)}
                helperText={formik.touched.Autor && formik.errors.Autor}
                className={classes.field}
                />
                <TextField
                fullWidth
                id="Cantidad"
                name="Cantidad"
                label="Cantidad"
                type="number"
                value={formik.values.Cantidad}
                onChange={formik.handleChange}
                error={formik.touched.Cantidad && Boolean(formik.errors.Cantidad)}
                helperText={formik.touched.Cantidad && formik.errors.Cantidad}
                className={classes.field}
                />
                <TextField
                fullWidth
                id="Precio"
                name="Precio"
                label="Precio"
                type="number"
                value={formik.values.Precio}
                onChange={formik.handleChange}
                error={formik.touched.Precio && Boolean(formik.errors.Precio)}
                helperText={formik.touched.Precio && formik.errors.Precio}
                className={classes.field}
                />


                <TextField
                fullWidth
                id="fotografia"
                name="fotografia"
                label="Image"
                type="file"
                value={formik.values.foto_uri}
                onChange={async (event) => {
                    console.log({event})
                    try {
                      const file = event.currentTarget.files[0]
                      const result = await getBase64(file)
                      setFotografia(result)
                    } catch(e) {
                        setFotografia("")
                    }
                  }}  
                error={formik.touched.foto_uri && Boolean(formik.errors.foto_uri)}
                helperText={formik.touched.foto_uri && formik.errors.foto_uri}
                />
                <div className={classes.buttoContainer}>
                    <Button color="primary" variant="contained" fullWidth type="submit">
                    { bookId ? 'Actualizar' : 'Crear'}
                    </Button>
                    <Button color="primary" variant="contained" fullWidth type="button" onClick={deleteAction}>
                    Eliminar
                    </Button>
                </div>
            </form>
        </Container>
    )
}

export default AddBook