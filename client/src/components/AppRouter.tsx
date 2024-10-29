import {Routes, Route, Navigate} from "react-router-dom"
import {IMPORT_PATH, routes} from "../consts/pages"

export default function AppRouter() {
  return (
    <Routes>
      {routes.map(({path, Component}) => (
        <Route key={path} path={path} element={<Component />} />
      ))}
      <Route path="*" element={<Navigate to={IMPORT_PATH} />} />
    </Routes>
  )
}