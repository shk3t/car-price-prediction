import styles from "../../styles/base.module.css"

interface NiceButtonProps extends React.ComponentProps<"button"> {
  very?: boolean
}

const defaultProps = {
  very: false,
}

export default function NiceButton(props: NiceButtonProps) {
  const {very, children, ...rest} = {...defaultProps, ...props}
  return (
    <button className={`${styles.niceButton} ${very && styles.very}`} {...rest}>
      {children}
    </button>
  )
}