import styles from "../../styles/base.module.css"

export default function VeryNiceInput(props: React.ComponentProps<"textarea">) {
  return <textarea className={styles.veryNiceInput} spellCheck={false} {...props}></textarea>
}