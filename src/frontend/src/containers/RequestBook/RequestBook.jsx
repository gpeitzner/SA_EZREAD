import { Container, FormGroup, TextField, Typography, Button, makeStyles } from '@material-ui/core'
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

const CREATE_URL=process.env.REACT_APP_REQUEST_FILE_CREATE_URL
const CREATE_REQUEST_URL=process.env.REACT_APP_REQUEST_FILE_CREATE__REQUEST_URL


const RequestBook = () => {
    console.log({CREATE_REQUEST_URL})
    const classes = useStyles()
    const [archivo, setArchivo] = React.useState(null)

    const formik = useFormik({
        initialValues: {
            nombre: '',
            autor: '',
            fecha: '',
            url: ''
        },
        onSubmit: async (values, setSubmitting) => {
            console.log({archivo, CREATE_URL})
            if(archivo){
                const bodyFormData = new FormData();
                bodyFormData.append('file', archivo); 
                const { status, data: fileData } = await axios({
                    method: "post",
                    url: CREATE_URL,
                    data: bodyFormData,
                    headers: { "Content-Type": "multipart/form-data" },
                })
                if (status === 200) {
                    const { url } = fileData
                    const nData = {
                        url,
                        nombre: values.nombre,
                        autor: values.autor,
                        fecha: values.fecha
                    }
                    const { status, data } = await axios({
                        method: "post",
                        url: CREATE_REQUEST_URL,
                        data: nData,
                    })

                    if (status === 200) {
                        alert('Su petición ha sido enviada.')
                    } else {
                        alert(data.message)
                    }

                } else {
                    alert(fileData.url)
                }
                setSubmitting(false)
            }

        },
      });


    return(
        <Container maxWidth="sm">
            <Typography component="h1" variant="h4">
                Solicitar libro
            </Typography>
            <Typography component="p" variant="subtitle1">
                Ingresa los datos de libro
            </Typography>
            <form className={classes.form} onSubmit={formik.handleSubmit}>
                <TextField
                fullWidth
                id="nombre"
                name="nombre"
                label="Nombre"
                value={formik.values.nombre}
                onChange={formik.handleChange}
                error={formik.touched.nombre && Boolean(formik.errors.nombre)}
                helperText={formik.touched.nombre && formik.errors.nombre}
                className={classes.field}
                />
                <TextField
                fullWidth
                id="autor"
                name="autor"
                label="Autor"
                value={formik.values.autor}
                onChange={formik.handleChange}
                error={formik.touched.autor && Boolean(formik.errors.autor)}
                helperText={formik.touched.autor && formik.errors.autor}
                className={classes.field}
                />
                <TextField
                fullWidth
                id="fecha"
                name="fecha"
                label="Fecha"
                value={formik.values.fecha}
                onChange={formik.handleChange}
                error={formik.touched.c && Boolean(formik.errors.c)}
                helperText={formik.touched.c && formik.errors.c}
                className={classes.field}
                />
                <TextField
                fullWidth
                id="file"
                name="file"
                label="Archivo"
                type="file"
                value={formik.values.foto_uri}
                onChange={async (event) => {
                    console.log({event})
                    try {
                      const file = event.currentTarget.files[0]
                      setArchivo(file)
                    } catch(e) {
                    }
                  }}  
                error={formik.touched.file && Boolean(formik.errors.file)}
                helperText={formik.touched.file && formik.errors.file}
                />
                <div className={classes.buttoContainer}>
                    <Button color="primary" variant="contained" fullWidth type="submit">
                    Crear
                    </Button>
                </div>
            </form>
        </Container>
    )
}

export default RequestBook