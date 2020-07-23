import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Lexicon.css';
import routes from '../constants/routes.json';

// type alias Props
type Props = {
  // TODO define actions
};

class WordRow extends React.Component {
    render() {
    const word = this.props.words.word;
    return (
      <tr>
        <td>{word.id}</td>
        <td>{word.pronunciation}</td>
        <td>{word.definition}</td>
        <td>{word.syntax}</td>
      </tr>
    )
  }
}

const FilterableWordTable = (props: Props) => (
// TODO
);

export default function Lexicon(props: Props) {
  const {} = props;

  return (
    <div>
      <div className={styles.backButton} data-tid="backButton">
        <Link to={routes.HOME}>
          <i className="fa fa-arrow-left fa-3x" />
        </Link>
      </div>
    </div>
  );
}
