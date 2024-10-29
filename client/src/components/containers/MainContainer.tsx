import styles from "../../styles/base.module.css"
import {ContainerMargins, availableMargins} from "../../types/component"

interface MainContainerProps extends React.ComponentProps<"main"> {
  flexEnabled: boolean
  vertical: boolean
  margin: ContainerMargins
}

function MainContainer(props: MainContainerProps) {
  const {flexEnabled, vertical, margin, children, ...rest} = props

  const containerStyles = flexEnabled
    ? vertical
      ? styles.vcenteringContainer
      : styles.centeringContainer
    : {}

  return (
    <main className={`${containerStyles} ${availableMargins[margin]}`} {...rest}>
      {children}
    </main>
  )
}

MainContainer.defaultProps = {
  flexEnabled: true,
  vertical: false,
  margin: ContainerMargins.DEFAULT,
}
export default MainContainer