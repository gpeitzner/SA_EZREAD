import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Login from './containers/Login'
import Register from './containers/Register'
import Main from './containers/Main'
import { RecoilRoot } from "recoil";



const App = () => {
  return (
    <RecoilRoot>
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
    </RecoilRoot>
  )

}


export default App;
