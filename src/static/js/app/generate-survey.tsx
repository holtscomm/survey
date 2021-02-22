import React from 'react';
import { render } from 'react-dom';

const GenerateSurvey = () => {
    const [email, setEmail] = React.useState('');
    const [firstName, setFirstName] = React.useState('');
    const [lastName, setLastName] = React.useState('');
    const [error, setError] = React.useState('');
    const [userId, setUserId] = React.useState('');
    const [surveyLink, setSurveyLink] = React.useState('');

    const createSurvey = (type: string, surveyLink: string) => {
        setError('');
        if (email === '' || firstName === '') {
            setError('Email and first name must be filled in!');
            return;
        }

        // Emulate a request to this API in the way it likes
        const params = new URLSearchParams();
        params.set('email', email);
        params.set('cart_details[0][name]', type);
        params.set('user_info[first_name]', firstName);
        params.set('user_info[last_name]', lastName);

        fetch('/api/v1/survey/purchase/', {
            method: 'POST',
            body: params
        })
            .then(response => response.json())
            .then(response => {
                setUserId(response.data.user_id);
                setSurveyLink(surveyLink);
            })
            .catch(() => setError('something failed with api request'));
    }

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-12">
                    <h1>Generate a paid survey:</h1>
                    {error !== '' && <div className="survey-page__info">{error}</div>}
                    <div className="form-group">
                        <label htmlFor="email">Email:</label>
                        <input type="email" className="form-control" value={email} onChange={ev => setEmail(ev.target.value)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="firstName">First Name:</label>
                        <input type="text" className="form-control" value={firstName} onChange={ev => setFirstName(ev.target.value)} />
                    </div>
                    <div className="form-group">
                        <label htmlFor="lastName">Last Name:</label>
                        <input type="text" className="form-control" value={lastName} onChange={ev => setLastName(ev.target.value)} />
                    </div>
                    <p>Clicking on a button below will generate that type of survey for the email and name you entered above.</p>
                    <button className="btn btn-primary" role="button" onClick={() => createSurvey('fullform', '')}>Full survey!</button>
                    <button className="btn btn-primary" role="button" onClick={() => createSurvey('short_a', '/a')}>Short form A survey!</button>
                    <button className="btn btn-primary" role="button" onClick={() => createSurvey('short_b', '/b')}>Short form B survey!</button>

                    {userId !== '' && (
                        <p className="bg-success">
                            <div>Done: new user id is <a target="_blank" href={`/gifts${surveyLink}/?userId=${userId}`}>{userId}</a>.</div>
                            <div>A task has been dispatched to send an email to {email}.</div>
                        </p>
                    )}
                </div>
            </div>
        </div>
    );
};

if (document.getElementById('generate-root') !== null) {
    render(<GenerateSurvey />, document.getElementById('generate-root'));
}