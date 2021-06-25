import { atom } from "recoil";

export const cartState = atom({
  key: 'cartState',
  default: {}
})

export const loginState = atom({
    key: 'loginState',
    default: {
      tipo: 'administrador',
      nombre: 'Editorial USAC'
    }
})