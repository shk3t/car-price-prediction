import headerStyles from "../styles/Header.module.css"
import {PREDICT_PATH, routes} from "../consts/pages"
import {Link} from "react-router-dom"
import githubImg from "../assets/github.png"
import eyeImg from "../assets/eye.png"

export default function Header() {
  return (
    <header>
      <div>
        <Link to={PREDICT_PATH} className={headerStyles.me}>
          <img src={eyeImg} />
          <span>
            shket<em>@</em>dev
          </span>
        </Link>
      </div>
      <div className={headerStyles.menu}>
        {routes.map(({path, title}) => (
          <Link key={path} to={path}>
            {title}
          </Link>
        ))}
      </div>
      <div>
        <a href={"https://github.com/shk3t/car-price-prediction"} className={headerStyles.git}>
          <img src={githubImg} />
        </a>
      </div>
    </header>
  )
}