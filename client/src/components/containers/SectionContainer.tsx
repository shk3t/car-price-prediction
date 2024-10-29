import styles from "../../styles/base.module.css"

function SectionContainer(props: React.ComponentProps<"div">) {
  const {children, ...rest} = props
  return (
    <section>
      <div className={styles.vcenteringContainer} {...rest}>
        {children}
      </div>
    </section>
  )
}

export default SectionContainer