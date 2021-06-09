import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Login from './containers/Login'
import Register from './containers/Register'
import Main from './containers/Main'



const App = () => {
  return (
    <Router>
      <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/register">
            <Register />
          </Route>
          <Route path="/">
            <Main />
          </Route>
        </Switch>
    </Router>
  )

}


export default App;
