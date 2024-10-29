import footerStyles from "../styles/Footer.module.css"
import blueEndImg from "../assets/blue-end.jpg"

export default function Footer() {
  return (
    <footer>
      <div className={footerStyles.gigaGap}>
        <p className={footerStyles.singleLabel}>{"<footer></footer>"}</p>
      </div>
      <img src={blueEndImg} />
    </footer>
  )
}