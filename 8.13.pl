#!/usr/bin/perl

# task: queue with max, any series of enqueue + dequeue + max = O(n)
# works only if there are no duplicates in the queue!!!

use strict;
use warnings;

package MyQueue;

sub new {
    my ($class, @values) = @_;
    my $self = { values => [], max => [] };
    bless $self => $class;
    for my $value (@values) { # this is not the main concern here, so even though I know it's not optimal, let me leave it as it is here
# could have just left an implementation with no values accepted in new()
        $self->enqueue($value);
    }
    return $self;
}

sub enqueue {
    my ($self, $value) = @_;
    push(@{$self->{values}}, $value);
    if (!defined($self->max)) {
        $self->{max} = [$value];
    }
    my $i;
    for ($i = scalar(@{$self->{max}})-1; $i >= 0 && $value >= $self->{max}[$i]; $i--) { pop(@{$self->{max}}) }
    $self->{max}[$i+1] = $value;
}

sub lookup {
    my $self = shift;
    return undef unless scalar(@{$self->{values}});
    return $self->{values}[0];
}

sub dequeue {
    my $self = shift;
    return undef unless scalar(@{$self->{values}});
    my $elem = shift(@{$self->{values}});
    my $next = $self->lookup;
    if ($elem == $self->max && (!defined($next) || $next < $self->max)) {
        shift(@{$self->{max}});
    }
    return $elem;
}

sub max {
    my $self = shift;
    return $self->{max}[0];
}

package TestMyQueue;

use Test::More;
use Test::Deep;
use Data::Dumper;

my $q = MyQueue->new(4);
is_deeply($q->{max}, [4], 'max set');
is($q->max, 4, 'max ok');
$q->enqueue(2); # 4,2
is_deeply($q->{max}, [4,2], 'max added');
is($q->max, 4, 'max ok');
$q->enqueue(1); # 4,2,1
is_deeply($q->{max}, [4,2,1], 'max added again');
is($q->max, 4, 'max ok');
$q->enqueue(3); # 4,2,1,3
is_deeply($q->{max}, [4,3], 'max modified now');
is($q->max, 4, 'max ok');
$q->enqueue(5);
is_deeply($q->{max}, [5], 'max cut down');
is($q->max, 5, 'max ok');
$q = MyQueue->new(4,2,1,5,7,3);
is($q->max, 7, 'max ok from start');
$q->dequeue();
is($q->max, 7, 'max still same');
$q->dequeue();
$q->dequeue();
$q->dequeue();
$q->dequeue();
is($q->max, 3, 'max changed');
$q->dequeue();
is($q->max, undef, 'no items left');
$q->enqueue(10);
is($q->max, 10, 'max started');
$q = MyQueue->new(3,1,2);
$q->dequeue();
is($q->max, 2);
$q = MyQueue->new(4,3,1,2,0);
$q->dequeue();
$q->dequeue();
is($q->max, 2);

done_testing;
