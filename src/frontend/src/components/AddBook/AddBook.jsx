import { Container, FormGroup, TextField, Typography, Button, makeStyles } from '@material-ui/core'
import * as React from 'react'
import { useFormik } from 'formik';
import { findByLabelText } from '@testing-library/dom';

const book = 
{
    "Editorial": "Espasa",
     "Titulo": "La Rebelión de las masas",
     "Genero": "Filosofía",
     "Autor" : "José Ortega y Gasset",
     "Activo": 1,
     "Cantidad" : 25,
     "id" :"60c0645b5a6ff4fc067a6bd3",
    // "Image":"https://enlinea.santotomas.cl/wp-content/uploads/sites/2/2020/10/Perros-mestizos.jpg"
     }


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

const AddBook = () => {
    const classes = useStyles()

    const formik = useFormik({
        initialValues: book,
        onSubmit: (values) => {
          alert(JSON.stringify(values, null, 2));
        },
      });



    return(
        <Container maxWidth="sm">
            <Typography component="h1" variant="h4">
                Crear libro
            </Typography>
            <Typography component="p" variant="subtitle1">
                Ingresa los datos de libro
            </Typography>
            <FormGroup className={classes.form}>
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
                id="Image"
                name="Image"
                label="Image"
                type="file"
                value={formik.values.Image}
                onChange={formik.handleChange}
                error={formik.touched.Image && Boolean(formik.errors.Image)}
                helperText={formik.touched.Image && formik.errors.Image}
                />
                <div className={classes.buttoContainer}>
                    <Button color="primary" variant="contained" fullWidth type="submit">
                    Crear
                    </Button>
                    <Button color="primary" variant="contained" fullWidth type="submit">
                    Eliminar
                    </Button>
                </div>
            </FormGroup>
        </Container>
    )
}

export default AddBook