import * as React from 'react'
import {
    Switch,
    Route,
    Link
  } from "react-router-dom";
import { makeStyles } from '@material-ui/core/styles';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Typography from '@material-ui/core/Typography';
import clsx from 'clsx';
import Badge from '@material-ui/core/Badge';
import ShoppingBasketIcon from '@material-ui/icons/ShoppingBasket';
import { AppBar, Toolbar } from '@material-ui/core';
import Drawer from '@material-ui/core/Drawer';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import Divider from '@material-ui/core/Divider';
import Container from '@material-ui/core/Container';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import AddBoxIcon from '@material-ui/icons/AddBox';
import BookIcon from '@material-ui/icons/Book';
import PeopleIcon from '@material-ui/icons/People';


const drawerWidth = 240;
const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex'
    },
    toolbar: {
        paddingRight: 24, // keep right padding when drawer closed
    },
    toolbarIcon: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'flex-end',
        padding: '0 8px',
        ...theme.mixins.toolbar,
    },
    appBar: {
        zIndex: theme.zIndex.drawer + 1,
        transition: theme.transitions.create(['width', 'margin'], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
        }),
        },
    appBarShift: {
        marginLeft: drawerWidth,
        width: `calc(100% - ${drawerWidth}px)`,
        transition: theme.transitions.create(['width', 'margin'], {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.enteringScreen,
        }),
        },
    menuButton: {
        marginRight: 36,
    },
    menuButtonHidden: {
        display: 'none',
    },
    title: {
        flexGrow: 1,
    },
    drawerPaper: {
        position: 'relative',
        whiteSpace: 'nowrap',
        width: drawerWidth,
        transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
        }),
    },
    drawerPaperClose: {
        overflowX: 'hidden',
        transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
        }),
        width: theme.spacing(7),
        [theme.breakpoints.up('sm')]: {
        width: theme.spacing(9),
        },
    },
    appBarSpacer: theme.mixins.toolbar,
    content: {
        flexGrow: 1,
        height: '100vh',
        overflow: 'auto',
    },
    container: {
        paddingTop: theme.spacing(4),
        paddingBottom: theme.spacing(4),
    },
      
}))


const Main = () => {
    const classes = useStyles()
    const [open, setOpen] = React.useState(false);

    const handleDrawerOpen = () => {
        setOpen(true);
      };

  const handleDrawerClose = () => {
    setOpen(false);
  };

    return ( <div className={classes.root}>
        <AppBar position="absolute" className={clsx(classes.appBar, open && classes.appBarShift)}>
            <Toolbar className={classes.toolbar}>
            <IconButton
            edge="start"
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            className={clsx(classes.menuButton, open && classes.menuButtonHidden)}
          >
            <MenuIcon />
          </IconButton>
          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
            EZRead
          </Typography>
          <IconButton color="inherit">
            <Badge badgeContent={0} color="secondary">
              <ShoppingBasketIcon />
            </Badge>
          </IconButton>
            </Toolbar>
        </AppBar>

      <Drawer
        variant="permanent"
        classes={{
          paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
        }}
        open={open}
      >
        <div className={classes.toolbarIcon}>
          <IconButton onClick={handleDrawerClose}>
            <ChevronLeftIcon />
          </IconButton>
        </div>
        <Divider />
        <List>
            <ListItem>
            <ListItemIcon>
                <Link to="/add-book">
                    <AddBoxIcon />
                </Link>
            </ListItemIcon>
            <Link to="/add-book">
                <ListItemText primary="add book" />
            </Link>
            </ListItem>
        </List>
        <Divider />
        <List>
        <ListItem>
            <ListItemIcon>
                <Link to="/users">
                    <PeopleIcon />
                </Link>
            </ListItemIcon>
            <Link to="/users">
                <ListItemText primary="Users" />
            </Link>
        </ListItem></List>
        <List>
        <ListItem>
            <ListItemIcon>
                <Link to="/">
                    <BookIcon />
                </Link>
            </ListItemIcon>
            <Link to="/">
                <ListItemText primary="Books" />
            </Link>
        </ListItem>
        </List>
        <Divider />
      </Drawer>
      <main className={classes.content}>
        <div className={classes.appBarSpacer} />
        <Container maxWidth="lg" className={classes.container}>
        <Switch>
          <Route path="/users">
            <div>books</div>
          </Route>
          <Route path="/add-book">
            <div>add-book</div>
          </Route>
          <Route path="/">
            <div>:)</div>
          </Route>
        </Switch>
        </Container>
      </main>
    </div> )
}

export default Main