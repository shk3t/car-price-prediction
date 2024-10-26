import {capitalize} from "lodash"
import styles from "../../styles/base.module.css"

interface NiceSelectProps extends React.ComponentProps<"select"> {
  options: any
}

export default function NiceSelect(props: NiceSelectProps) {
  return (
    <select className={styles.niceSelect} {...props}>
      {Object.values(props.options).map((value: any) => (
        <option key={value} value={value}>
          {capitalize(value)}
        </option>
      ))}
    </select>
  )
}