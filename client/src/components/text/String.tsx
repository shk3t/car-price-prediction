import styles from "../../styles/base.module.css"

export default function StringSpan(props: React.ComponentProps<"span">) {
  return <span className={styles.stringSpan} {...props}></span>
}