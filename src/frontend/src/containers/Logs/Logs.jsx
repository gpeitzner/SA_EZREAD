import * as React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardContent, Container, IconButton, Typography } from '@material-ui/core';
import GroupAddIcon from '@material-ui/icons/GroupAdd';
import DeleteIcon from '@material-ui/icons/Delete';
import axios from 'axios'
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles({
    table: {
      minWidth: 650,
    },
  });
  

const GET_URL = process.env.REACT_APP_LOGS_GET_URL

const Users = () => {
    const classes = useStyles()
    const [logs, setLogs] = React.useState([])

    React.useEffect(() => {
        const getAsync = async () => {
            try {
              const { status, data } = await axios.get(GET_URL)
              if (status === 200) {
                  if(data.logs)
                    setLogs(data.logs)
              } else {
                  alert(data.message)
              }
            } catch(e) {
              alert('Login no exitoso')
            }
        }
        getAsync()
    }, [])

    
    return(
        <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell align="center">Fecha</TableCell>
            <TableCell align="center">Operacion</TableCell>
            <TableCell align="center">Libro</TableCell>
            <TableCell align="center">Editorial</TableCell>
            <TableCell align="center">Descripcion</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {logs.map((row) => (
            <TableRow key={row.id}>
              <TableCell align="center">{row.Fecha}</TableCell>
              <TableCell align="center">{row.Operacion}</TableCell>
              <TableCell align="center">{row.Libro}</TableCell>
              <TableCell align="center">{row.Editorial}</TableCell>
              <TableCell align="center">{row.Descripcion}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
    )
}

export default Users