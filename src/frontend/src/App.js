import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Login from './containers/Login'
import Register from './containers/Register'




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
            <div />
          </Route>
        </Switch>
    </Router>
  )

}


export default App;
