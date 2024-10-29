import styles from "../../styles/base.module.css"

interface ContainerProps extends React.ComponentProps<"div"> {
  vertical?: boolean
  frame?: boolean
}

const defaultProps = {
  vertical: false,
  frame: false,
}

export default function CenteringContainer(props: ContainerProps) {
  const {vertical, frame, onClick, children, ...rest} = {...defaultProps, ...props}
  return (
    <div
      className={`${vertical ? styles.vcenteringContainer : styles.centeringContainer} ${
        frame && styles.frame
      } ${onClick && styles.clickable}`}
      onClick={onClick}
      {...rest}
    >
      {children}
    </div>
  )
}