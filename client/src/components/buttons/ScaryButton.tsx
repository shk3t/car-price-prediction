import styles from "../../styles/base.module.css"

export default function ScaryButton(props: React.ComponentProps<"button">) {
  const {children, ...rest} = props
  return (
    <button className={styles.scaryButton} {...rest}>
      {children}
    </button>
  )
}